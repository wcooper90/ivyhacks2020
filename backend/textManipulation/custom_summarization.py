from transformers import *

# Load model, model config and tokenizer via Transformers
custom_config = AutoConfig.from_pretrained('allenai/scibert_scivocab_uncased')
custom_config.output_hidden_states=True
custom_tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
custom_model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased', config=custom_config)

from summarizer import Summarizer

body = """World War II (WWII or WW2), also known as the Second World War, was a global war that lasted from 1939 to 1945. It involved the vast majority of the world's countries—including all the great powers—forming two opposing military alliances: the Allies and the Axis. In a state of total war, directly involving more than 100 million people from more than 30 countries, the major participants threw their entire economic, industrial, and scientific capabilities behind the war effort, blurring the distinction between civilian and military resources. World War II was the deadliest conflict in human history, marked by 70 to 85 million fatalities. Tens of millions of people died due to genocides (including the Holocaust), premeditated death from starvation, massacres, and disease. Aircraft played a major role in the conflict, including in the use of strategic bombing of population centres, and the only uses of nuclear weapons in war.

World War II is generally considered to have begun on 1 September 1939, with the invasion of Poland by Germany and subsequent declarations of war on Germany by France and the United Kingdom. From late 1939 to early 1941, in a series of campaigns and treaties, Germany conquered or controlled much of continental Europe, and formed the Axis alliance with Italy and Japan. Under the Molotov–Ribbentrop Pact of August 1939, Germany and the Soviet Union partitioned and annexed territories of their European neighbours: Poland, Finland, Romania and the Baltic states. Following the onset of campaigns in North Africa and East Africa, and the Fall of France in mid-1940, the war continued primarily between the European Axis powers and the British Empire, with war in the Balkans, the aerial Battle of Britain, the Blitz, and the Battle of the Atlantic. On 22 June 1941, Germany led the European Axis powers in an invasion of the Soviet Union, opening the largest land theatre of war in history and trapping the Axis, crucially the German Wehrmacht, in a war of attrition.

Japan, which aimed to dominate Asia and the Pacific, was at war with the Republic of China by 1937. In December 1941, Japan launched a surprise attack on the United States as well as European colonies in East Asia and the Pacific. Following an immediate US declaration of war against Japan, supported by one from the UK, the European Axis powers declared war on the United States in solidarity with their ally. Japan soon captured much of the Western Pacific, but its advances were halted in 1942 after losing the critical Battle of Midway; later, Germany and Italy were defeated in North Africa and at Stalingrad in the Soviet Union. Key setbacks in 1943—including a series of German defeats on the Eastern Front, the Allied invasions of Sicily and Italy, and Allied offensives in the Pacific—cost the Axis its initiative and forced it into strategic retreat on all fronts. In 1944, the Western Allies invaded German-occupied France, while the Soviet Union regained its territorial losses and turned towards Germany and its allies. During 1944 and 1945, Japan suffered reversals in mainland Asia, while the Allies crippled the Japanese Navy and captured key Western Pacific islands.

The war in Europe concluded with an invasion of Germany by the Western Allies and the Soviet Union, culminating in the capture of Berlin by Soviet troops, the suicide of Adolf Hitler and the German unconditional surrender on 8 May 1945. Following the Potsdam Declaration by the Allies on 26 July 1945 and the refusal of Japan to surrender on its terms, the United States dropped atomic bombs on the Japanese cities of Hiroshima and Nagasaki on 6 and 9 August, respectively. Faced with an imminent invasion of the Japanese archipelago, the possibility of additional atomic bombings, and the Soviet entry into the war against Japan and its invasion of Manchuria on 9 August, Japan announced its intention to surrender on 15 August 1945, cementing total victory in Asia for the Allies. In the wake of the war, Germany and Japan were occupied and war crimes tribunals were conducted against German and Japanese leaders.

World War II changed the political alignment and social structure of the globe. The United Nations (UN) was established to foster international co-operation and prevent future conflicts, and the victorious great powers—China, France, the Soviet Union, the United Kingdom, and the United States—became the permanent members of its Security Council. The Soviet Union and the United States emerged as rival superpowers, setting the stage for the nearly half-century-long Cold War. In the wake of European devastation, the influence of its great powers waned, triggering the decolonisation of Africa and Asia. Most countries whose industries had been damaged moved towards economic recovery and expansion. Political integration, especially in Europe, began as an effort to forestall future hostilities, end pre-war enmities and forge a sense of common identity."""


model = Summarizer(custom_model=custom_model, custom_tokenizer=custom_tokenizer)

result = model(body)
result = ''.join(result)
print(result)